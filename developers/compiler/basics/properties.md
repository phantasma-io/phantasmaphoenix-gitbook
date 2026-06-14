# Properties

Properties such as

1. `name`: The name of the Token.
2. `symbol`: Symbol of the token, should be equal to the token declaration.
3. `isBurnable`: Whether the token can be burned.
4. `isFinite`: If it is finite
5. `isFungible`: If is Fungible (If it is an NFT, should be equals to false)
6. `maxSupply`: The maximum supply of that token
7. `isTransferable`: Allow the NFT/Token to be transfered.
8. `isDivisible`: Whether token amounts can have decimal places.
9. `decimals`: The number of decimals



```csharp
property name: string = "Example";
property symbol: string = "EXP";
property isBurnable: bool = true;
property isFinite: bool = true;
property isFungible: bool = false;
property maxSupply: number = 10000;
property isTransferable: bool = true;
property isDivisible: bool = true;
property decimals:number = 8;
```
