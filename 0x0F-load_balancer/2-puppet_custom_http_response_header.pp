# Automate way to create a custom HTTP header response
exec {'command':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
}

file_line { 'add_header':
  ensure=> 'present',
  path  => '/etc/nginx/sites-available/default',
  match => '^server {',
  line  => "server {\n\tadd_header X-Served-By ${hostname};",
}

exec {'nginx restart':
  command => '/usr/sbin/service nginx restart',
}
