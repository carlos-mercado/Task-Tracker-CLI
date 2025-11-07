let
    pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
    packages = [
    (pkgs.python3.withPackages (python-pkgs: [
        #python-pkgs.json
        # Add other Python packages here, e.g., python-pkgs.numpy
    ]))
    ];
}
