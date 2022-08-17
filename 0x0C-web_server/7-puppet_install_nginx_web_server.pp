# configuring your server with Puppet! Just as you did before

package { 'nginx':
}
 
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'redirect permaently 301':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}