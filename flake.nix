{
  description = "Competitive programming development shell";

  # This revision provides GCC 15.2.0 alongside PyPy 3.11.
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/b153953686370a8dc14231db115b058b137644de";
  inputs.atcoder-cli = {
    url = "github:Tatamo/atcoder-cli/v2.2.0";
    flake = false;
  };

  outputs = inputs@{ nixpkgs, ... }:
    let
      systems = [ "aarch64-darwin" "x86_64-darwin" "aarch64-linux" "x86_64-linux" ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in
    {
      devShells = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };
          atcoderCli = pkgs.buildNpmPackage {
            pname = "atcoder-cli";
            version = "2.2.0";
            src = inputs.atcoder-cli;
            npmDepsHash = "sha256-ufG7Fq5D2SOzUp8KYRYUB5tYJYoADuhK+2zDfG0a3ks=";

            # nixpkgs has no acc package; build the locked upstream source here.
            # fsevents is an optional watcher whose legacy Node ABI fails on Node 24.
            npmInstallFlags = [ "--omit=optional" ];
            npmRebuildFlags = [ "--ignore-scripts" ];

            # The upstream webpack 4 build needs OpenSSL's legacy provider.
            NODE_OPTIONS = "--openssl-legacy-provider";
          };
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python311
              pypy311
              gcc15
              online-judge-tools
              nodejs
              atcoderCli
            ];

            # Use `g++ -std=c++23` for the requested contest language standard.
          };
        });
    };
}
