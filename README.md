# XSS-Mole
Lightweight (blind) XSS Server. The mole does not see well. But it does it's thing.

Other projects like xsshunter-go or original xsshunter are probably what you're looking for, in the unlikely case you ended up here. 
I cant code fo shite.

## Why?
Did not want too many components when testing for blind XSS.
Always asked myself "do i need all this tho?" when configuring dockerfiles from other projects.
This is a bare minimum where you can:
- Spin up an interact.sh server || specify your domain
- Log the XSS requests. Stored in file or SQLite.
- Generate blind XSS requests based on your domain.
- You can use it by just running it raw or use simple Dockerfile without too much dependencies.
- Just to learn more Go :)

