# Mail



| Method                                                           | Return type | Description                                                   |
| ---------------------------------------------------------------- | ----------- | ------------------------------------------------------------- |
| Mail.pushMessage(from:Address, target:Address, archiveHash:Hash) | None        | To push a message to the target user mailbox.                 |
| Mail.domainExists(domainName:String)                             | Bool        | Returns true if the specified domain exists, false otherwise. |
| Mail.registerDomain(from:Address, domainName:String)             | None        | To register a domain, from an address and a domain name.      |
| Mail.unregisterDomain(domainName:String)                         | None        | To unregister a domain name.                                  |
| Mail.migrateDomain(domainName:String, target:Address)            | None        | To migrate a domain to a new Address.                         |
| Mail.joinDomain(from:Address, domainName:String)                 | None        | To a user join a domain.                                      |
| Mail.leaveDomain(from:Address, domainName:String)                | None        | To a user leave a domain.                                     |
| Mail.getUserDomain(target:Address)                               | String      | To the the user domain.                                       |
