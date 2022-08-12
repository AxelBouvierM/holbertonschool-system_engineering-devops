# Using Puppet, create a manifest that kills a process named killmenow
exec { 'kilmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell', }