#!/bin/sh
# Regenerate the General Liquidity Python SDK from the OpenAPI spec.
#
# openapi-generator emits the package as `general_liquidity/` at the output root.
# This repo uses a src-layout, so the generated package is relocated under src/.
# The generated code (src/general_liquidity/), docs/, and test/ are refreshed;
# packaging files (pyproject.toml, setup.py, README, ...) are hand-maintained.
#
# Reproducibility: the generator jar is pinned by version and sha256. It is
# fetched to a gitignored cache and checksum-verified before use. A local jar can
# be supplied via JAR= (it is verified against the same checksum). The spec is
# read from the vendored copy under openapi/ so CI needs only this repo.
set -eu

GENERATOR_VERSION="7.11.0"
# sha256 of openapi-generator-cli-7.11.0.jar from Maven Central. Verified against
# the published .sha1/.md5 and by recomputing sha256 on a fresh download.
GENERATOR_SHA256="113c25df5a781d5a1fc2b883f12fe8f263db285ab12e15854d5b15306e1bf7fc"
JAR_URL="https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${GENERATOR_VERSION}/openapi-generator-cli-${GENERATOR_VERSION}.jar"

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CACHE_DIR="$REPO_ROOT/.codegen-cache"
SPEC="${SPEC:-$REPO_ROOT/openapi/openapi.yaml}"

PKG="general_liquidity"

# sha256 of a file, portable across sha256sum / shasum / openssl.
checksum() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | cut -d' ' -f1
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1" | cut -d' ' -f1
  else
    openssl dgst -sha256 "$1" | awk '{print $NF}'
  fi
}

verify_jar() {
  got="$(checksum "$1")"
  if [ "$got" != "$GENERATOR_SHA256" ]; then
    echo "checksum mismatch for $1" >&2
    echo "  expected $GENERATOR_SHA256" >&2
    echo "  got      $got" >&2
    return 1
  fi
}

# Resolve the jar: caller override (JAR=) or the pinned, cached download.
if [ -n "${JAR:-}" ]; then
  if [ ! -f "$JAR" ]; then
    echo "JAR override not found at: $JAR" >&2
    exit 1
  fi
else
  JAR="$CACHE_DIR/openapi-generator-cli-${GENERATOR_VERSION}.jar"
  if [ ! -f "$JAR" ]; then
    mkdir -p "$CACHE_DIR"
    echo "Fetching openapi-generator $GENERATOR_VERSION ..." >&2
    if command -v curl >/dev/null 2>&1; then
      curl -fsSL -o "$JAR" "$JAR_URL"
    elif command -v wget >/dev/null 2>&1; then
      wget -q -O "$JAR" "$JAR_URL"
    else
      echo "need curl or wget to fetch the generator jar" >&2
      exit 1
    fi
  fi
fi

verify_jar "$JAR"

if [ ! -f "$SPEC" ]; then
  echo "OpenAPI spec not found at: $SPEC" >&2
  echo "Set SPEC=/path/to/openapi.yaml" >&2
  exit 1
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

java -jar "$JAR" generate \
  -i "$SPEC" \
  -g python \
  -o "$TMP" \
  --git-user-id general-liquidity \
  --git-repo-id general-liquidity-python \
  --additional-properties="packageName=$PKG,projectName=general-liquidity"

# Hand-authored modules that live INSIDE the generated package directory. The relocation
# below replaces that directory wholesale, so they are carried across it. Without this the
# operator signing seam is deleted on every regeneration, and the codegen drift gate fails
# on a deletion the script itself caused.
HAND_WRITTEN="operator.py"

# Relocate the generated package into the src-layout.
KEEP="$(mktemp -d)"
for f in $HAND_WRITTEN; do
  [ -f "$REPO_ROOT/src/$PKG/$f" ] && cp "$REPO_ROOT/src/$PKG/$f" "$KEEP/$f"
done
rm -rf "$REPO_ROOT/src/$PKG"
mkdir -p "$REPO_ROOT/src"
cp -R "$TMP/$PKG" "$REPO_ROOT/src/$PKG"
for f in $HAND_WRITTEN; do
  [ -f "$KEEP/$f" ] && cp "$KEEP/$f" "$REPO_ROOT/src/$PKG/$f"
done
rm -rf "$KEEP"

if [ -d "$TMP/docs" ]; then
  rm -rf "$REPO_ROOT/docs"
  cp -R "$TMP/docs" "$REPO_ROOT/docs"
fi
if [ -d "$TMP/test" ]; then
  rm -rf "$REPO_ROOT/test"
  cp -R "$TMP/test" "$REPO_ROOT/test"
fi

echo "Regenerated src/$PKG from $SPEC"
echo "Run: pip install -e . && pytest"
