# Logging in to the Wallet

This is the documentation for the `OnLogin()` method, which is used to connect and log in to the wallet using the Phantasma Link SDK.

#### Method Description

The `OnLogin()` method is responsible for connecting and logging in to the wallet. It checks if the Phantasma Link Client is ready and not logged in, then proceeds to initiate the login process. If successful, it triggers the `OnLoginEvent` with a success message; otherwise, it provides an appropriate error message.

#### Method Usage

```csharp
/// <summary>
/// Method used to connect to the wallet.
/// </summary>
public void OnLogin()
{
    // Check if the Phantasma Link Client is ready
    if (PhantasmaLinkClient.Instance.Ready)
    {
        // Check if the user is not already logged in
        if (!PhantasmaLinkClient.Instance.IsLogged)
            // Attempt to log in
            PhantasmaLinkClient.Instance.Login((result, msg) =>
            {
                // If the login is successful
                if (result)
                {
                    // Trigger the OnLoginEvent with a success message
                    OnLoginEvent?.Invoke("Logged In.", false);
                    Debug.LogWarning("Phantasma Link authorization logged.");
                }
                else
                {
                    // Trigger the OnLoginEvent with an error message
                    OnLoginEvent?.Invoke("Phantasma Link authorization failed.", true);
                    Debug.LogWarning("Phantasma Link authorization failed.");
                }
            });
        else
            // If the user is already logged in, trigger the OnLoginEvent with a success message
            OnLoginEvent?.Invoke("Logged In.", false);
    }
    else
    {
        // If the Phantasma Link Client is not ready, display a warning and trigger the OnLoginEvent with an error message
        Debug.LogWarning("Phantasma Link connection is not ready.");
        OnLoginEvent?.Invoke("Phantasma Link connection is not ready.", true);
        PhantasmaLinkClient.Instance.Enable();
    }
}
```

