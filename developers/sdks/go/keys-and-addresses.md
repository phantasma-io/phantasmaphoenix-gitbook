# Go SDK Keys And Addresses

`pkg/cryptography` contains the key, address, signature, WIF, and hash types
used by the Go SDK.

## Generate Or Import Keys

```go
keys, err := cryptography.GeneratePhantasmaKeys()
if err != nil {
    return err
}

sameKeys, err := cryptography.FromWIF(keys.WIF())
if err != nil {
    return err
}

fmt.Println(sameKeys.Address().String())
```

Keep WIF values outside logs, browser bundles, and repository files. Local
signing helpers are for trusted services, CLIs, tests, and operator tooling.

## Address Parsing

```go
addr, err := cryptography.FromString("P...")
if err != nil {
    return err
}

if !cryptography.IsValidAddress(addr.String()) {
    return fmt.Errorf("invalid address")
}
```

High-level script helpers take `cryptography.Address` values. Raw strings passed
to low-level VM calls are encoded as VM strings, not address bytes.

## Carbon `Bytes32`

Carbon messages identify accounts by 32-byte public keys or Carbon address
values. Convert Phantasma keys and addresses with the Carbon helpers:

```go
owner, err := carbon.Bytes32FromPublicKey(keys.PublicKey())
receiver, err := carbon.Bytes32FromPhantasmaAddressText("P...")
```

Use `Must...` helpers only for constants and tests. For user input, call the
checked function and return the error to the caller.
