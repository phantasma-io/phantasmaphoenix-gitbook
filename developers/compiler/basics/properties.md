# Properties

A `token` module declares its token through properties. The validator reads
them when the token is created or attached, by calling the getter the compiler
emits for each property.

| Property | Type | Read by the validator |
| --- | --- | --- |
| `name` | string | Required. The token name. |
| `symbol` | string | The symbol; it is taken from the `token SYMBOL` declaration and does not need a property. |
| `isTransferable` | bool | Sets the `Transferable` flag. |
| `isFungible` | bool | Sets the `Fungible` flag. An NFT token sets it to `false`. |
| `isFinite` | bool | Sets the `Finite` flag. A finite token also needs `maxSupply`. |
| `isDivisible` | bool | Sets the `Divisible` flag. An NFT token cannot be divisible. |
| `isBurnable` | bool | Sets the `Burnable` flag. |
| `isMintable` | bool | Sets the `Mintable` flag. |
| `isStakable`, `isFiat` | bool | Set the `Stakable` and `Fiat` flags. |
| `maxSupply` | number | The maximum supply, read when the token is finite. |
| `decimals` | number | The number of decimals, 0 to 255. An NFT token uses 0. |

At least one flag must be set. `isFuel` is reserved for KCAL and `isSwappable`
cannot be set at creation.

```csharp
token EXP {
    property name: string = "Example";
    property isBurnable: bool = true;
    property isFinite: bool = true;
    property isFungible: bool = true;
    property isDivisible: bool = true;
    property isTransferable: bool = true;
    property maxSupply: number = 10000;
    property decimals: number = 8;
}
```

An NFT token can also declare `description`, `imageURL`, `infoURL` and
`royalties` properties inside its `nft` submodules; see the NFT example on the
[Examples](../examples/README.md) page.
