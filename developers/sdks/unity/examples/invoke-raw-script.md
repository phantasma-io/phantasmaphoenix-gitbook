# Invoke Raw Script

{% hint style="info" %}
Current RPC and Unity SDK source expose `InvokeRawScript` as a read-only VM execution call. The example does not require transaction signing or a wallet prompt.
{% endhint %}

This example shows how to call the blockchain directly to get information using the `InvokeRawScript()` method from the `PhantasmaAPI` class. A script is created and encoded before being passed to the method.

```csharp
public void InvokeRawScript()
{
    PhantasmaAPI api = new PhantasmaAPI("https://testnet.phantasma.info/rpc");
    var account = Address.Parse("P2KKEjZK7AbcKZjuZMsWKKgEjNzeGtr2zBiV7qYJHxNXvUa");
    ScriptBuilder sb = new ScriptBuilder();
    var script = sb.
        CallContract("stake", "GetUnclaimed", account).
        EndScript();
    var scriptEncoded = Base16.Encode(script);
    StartCoroutine(api.InvokeRawScript("main", scriptEncoded, scriptResult =>
    {
        // The KCAL atoms the account can claim from its SOUL stake.
        var unclaimed = VMObject.FromBytes(Base16.Decode(scriptResult.Results[0])).AsNumber();
        Debug.Log(unclaimed);
    }));
}
```
