# Smart Contracts

Phantasma supports VM smart contracts. In the current toolchain, contracts are authored in TOMB source files and compiled with `pha-tomb`.

Smart-contract workflows fall into two broad groups:
- standalone custom contracts
- token-backed contracts bound to an uppercase token symbol

{% content-ref url="/developers/compiler" %}
TOMB Compiler
{% endcontent-ref %}

## Deployment flows

- standalone lowercase custom contract -> deploy with `contract deploy`
- new uppercase token-backed contract -> create with `--create-token`
- existing token + new VM code -> `contract attach`
- later contract code update -> `contract upgrade`

For the current deployment tooling:

{% content-ref url="/developers/tools/pha-deploy.md" %}
pha-deploy
{% endcontent-ref %}

For the deployment flow overview:

{% content-ref url="how-to-deploy.md" %}
How to Deploy
{% endcontent-ref %}
