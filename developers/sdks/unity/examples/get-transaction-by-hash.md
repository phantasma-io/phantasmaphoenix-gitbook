# Get Transaction by Hash

This example demonstrates fetching a transaction's details by its hash. The `GetTransaction()` method from the `PhantasmaAPI` class is used to retrieve the transaction details, which are then passed to the provided callback.

```csharp
public void GetTransactionByHash()
{
    var api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
    var hash = "9749DCDAA37A53397AFB4EA30547C40BBF6ACC5B89B0234737C7A5AF71B0D4F2";

    StartCoroutine(api.GetTransaction(hash,
        (txResult) =>
        {
            Debug.Log($"[Tx] Hash: {txResult.Hash}, State: {txResult.State}");
        },
        (errorCode, errorMessage) =>
        {
            Debug.LogError($"[Error][{errorCode}] {errorMessage}");
        }
    ));
}
```
