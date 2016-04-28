# Build for profiling

    stack build --executable-profiling --library-profiling --ghc-options="-rtsopts"
    stack exec ch25 1e7  -- +RTS -sstderr