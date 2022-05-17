This week’s short newsletter summarizes a Bitcoin Core PR Review Club meeting and describes an update to Rust Bitcoin.

## News

No significant news this week. Topics we’ve previously covered, including [OP_CHECKTEMPLATEVERIFY](https://bitcoinops.org/en/topics/op_checktemplateverify/) and [SIGHASH_ANYPREVOUT](https://bitcoinops.org/en/topics/sighash_anyprevout/), did receive many additional comments—but much of the conversation was either non-technical or about minor details that we don’t consider broadly relevant. Several interesting posts to the developer mailing lists were received while this issue of the newsletter was being edited; we will cover them in detail next week.

## Bitcoin Core PR Review Club

*In this monthly section, we summarize a recent [Bitcoin Core PR Review Club](https://bitcoincore.reviews/) meeting, highlighting some of the important questions and answers. Click on a question below to see a summary of the answer from the meeting.*

[Improve Indices on pruned nodes via prune blockers](https://bitcoincore.reviews/21726) is a PR by Fabian Jahr to introduce a new method for deciding when it is safe to prune a block from block storage. This new method enables pruning nodes to maintain a Coinstats index and removes the validation module’s dependency on index-related code.


## Notable code and documentation changes

*Notable changes this week in [Bitcoin Core](https://github.com/bitcoin/bitcoin), [Core Lightning](https://github.com/ElementsProject/lightning), [Eclair](https://github.com/ACINQ/eclair), [LDK](https://github.com/lightningdevkit/rust-lightning), [LND](https://github.com/lightningnetwork/lnd/), [libsecp256k1](https://github.com/bitcoin-core/secp256k1), [Hardware Wallet Interface (HWI)](https://github.com/bitcoin-core/HWI), [Rust Bitcoin](https://github.com/rust-bitcoin/rust-bitcoin), [BTCPay Server](https://github.com/btcpayserver/btcpayserver/), [BDK](https://github.com/bitcoindevkit/bdk), [Bitcoin Improvement Proposals (BIPs)](https://github.com/bitcoin/bips/), and [Lightning BOLTs](https://github.com/lightning/bolts).*

- [●](https://bitcoinops.org/en/newsletters/2022/05/11/#rust-bitcoin-716) [Rust Bitcoin #716](https://github.com/rust-bitcoin/rust-bitcoin/issues/716) Added `amount::Display`, a configurable Display type for denominations or other user-facing amounts. This patch reduces all representations of numbers to the minimum width by default, thereby reducing the use of superfluous zeros that caused [BIP21](https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki) URIs to be needlessly longer, which often made QR codes larger or harder to scan than necessary.