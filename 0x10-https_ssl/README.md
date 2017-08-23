# HTTPS SSL

## CONCEPTS
- HTTPS : Hyper Text Transfer Protocol is a secure version of HTTP, the protocol over which data is sent between your browser and website. HTTPS page typically uses one of the two secure protocols to encrypt communications- SLL or TLS. Both TLS and SSL protocols use what is known as Asymmentric public Key Infrastructure(PKI) system. Asymmetric system uses two keys- public and Private key . Anything encrypted with public key can only be decrypted with a private key.
When an HTTPS connection is requested, the website will send its SSL certificate to the browser. This certificate contains public key needed to begin the secure connection. Then SSL handshake takes place, which involves generation of shared secrets to establish a uniquely secured connection between browser and the website.
Benefits of HTTPS are mainly that the connection is encrypted and cannot be intercepted.
Disadvantage is that it is costly.Performance is another disadvantage. 
