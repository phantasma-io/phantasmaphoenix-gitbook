# Organization

{% hint style="info" %}
The Organization library allows access to methods to handle [DAOs](https://docs.phantasma.info/#chain-organizations)
{% endhint %}

| Method                                                                  | Return type | Description                                                                                    |
| ----------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------- |
| Organization.create(from:Address, id:String, name:String, script:Bytes) | None        | Creates a new DAO. The creator address will be automatically added as part of the DAO members. |
| Organization.addMember(from:Address, name:String, target:Address)       | None        | Adds a new member to a DAO.                                                                    |

\
