# Get Account Balances

This example demonstrates how to retrieve the balances of the logged-in account. It checks if the user is logged in and then calls the `GetAccount()` method from the `PhantasmaAPI` class to fetch the account details. The number of balances is then logged to the console.

```csharp
public void GetBalances()
{
    if (!PhantasmaLinkClient.Instance.IsLogged) return;
        
    PhantasmaAPI api = new PhantasmaAPI("https://testnet.phantasma.io/rpc");
    StartCoroutine(api.GetAccount(PhantasmaLinkClient.Instance.Address, account =>
    {
        Debug.Log(account.balances.Length);
    }));
}
```
