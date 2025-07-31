# Governance

{% hint style="info" %}
The Governance library allows to interact with the decentralized [governance](https://docs.phantasma.io/#chain-governance) of Phantasma.
{% endhint %}

| Method                                                                           | Return type | Description                                                                                                                        |
| -------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Governance.hasName(name:String)                                                  | bool        | Returns true if a specific governance tag exists, false otherwise.                                                                 |
| Governance.createValue(name:String, initial:Number, serializedConstraints:Bytes) | None        | Creates a new governance tag and assigns an inital value to it, alongside optional contraints.                                     |
| Governance.getValue(name:String)                                                 | Number      | Returns the current value of a governance tag.                                                                                     |
| Governance.setValue(name:String, value:Number)                                   | None        | Alters the value of a governance tag. Consensus on the change must be achieved before calling this method, otherwise it will fail. |

\
