# Stake

| Method                                                                               | Return type | Description                                                                      |
| ------------------------------------------------------------------------------------ | ----------- | -------------------------------------------------------------------------------- |
| Stake.getMasterThreshold()                                                           | Number      | Equivalent to calling Governance.getValue() for "MasterStakeThresholdTag".       |
| Stake.isMaster(address:Address)                                                      | bool        | Returns true if the specified address is a SOUL master, returns false otherwise. |
| Stake.getMasterCount()                                                               | Number      | Return current number of SOUL masters.                                           |
| Stake.getClaimMasterCount(claimDate:Timestamp)                                       | Number      | Returns how much SOUL is claimable via a master claim.                           |
| Stake.getMasterClaimDate(claimDistance:Number)                                       | Timestamp   | TODO                                                                             |
| Stake.getMasterDate(target:Address)                                                  | Timestamp   | TODO                                                                             |
| Stake.getMasterClaimDateFromReference(claimDistance:Number, referenceTime:Timestamp) | Timestamp   | TODO                                                                             |
| Stake.getMasterRewards(address:Address)                                              | Number      | TODO                                                                             |
| Stake.masterClaim(from:Address)                                                      | None        | TODO                                                                             |
| Stake.stake(from:Address, stakeAmount:Number)                                        | None        | To stake an amount to the the address with the stake amount.                     |
| Stake.unstake(from:Address, unstakeAmount:Number)                                    | None        | To unstake an amount to the the address with the unstake amount.                 |
| Stake.getTimeBeforeUnstake(from:Address)                                             | Number      | TODO                                                                             |
| Stake.getStakeTimestamp(from:Address)                                                | Timestamp   | Returns timestamp of last stake for the specified address.                       |
| Stake.getUnclaimed(from:Address)                                                     | Number      | Returns the unclaimed KCAL amount for the specified address.                     |
| Stake.claim(from:Address, stakeAddress:Address)                                      | None        | Claims the the staked rewards for the given stake address.                       |
| Stake.getStake(address:Address)                                                      | Number      | Returns how much SOUL is staked at the specified address.                        |
| Stake.getStorageStake(address:Address)                                               | Number      | Returns how much SOUL is locked due to being used for storage.                   |
| Stake.fuelToStake(fuelAmount:Number)                                                 | Number      | Converts KCAL amount to SOUL.                                                    |
| Stake.stakeToFuel(stakeAmount:Number)                                                | Number      | Converts SOUL amount to KCAL.                                                    |
| Stake.getAddressVotingPower(address:Address)                                         | Number      | Returns the normalized voting power of an address.                               |

\
