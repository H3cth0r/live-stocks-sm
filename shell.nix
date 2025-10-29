{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.gcc
    pkgs.zlib

    pkgs.postgresql
    pkgs.redis
  ];

  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib 
      pkgs.zlib
    ]}"

    # --- Virtual environment setup ---
    if [ ! -d ".venv" ]; then
      echo "Creating Python virtual environment in ./.venv..."
      python -m venv .venv
    fi

    source .venv/bin/activate

    echo "Installing packages from requirements.txt..."
    pip install -r requirements.txt

    echo ""
    echo "Python virtual environment is ready and activated."
  '';
}
