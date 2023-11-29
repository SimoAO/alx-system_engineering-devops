# Install and configure an Nginx server using puppet
package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

exec { 'redirection':
  command => "/usr/bin/sed -i '/^}$/i \\\n\tlocation \\/redirect_me {return 301 https:\\/\\/www.youtube.com\\/watch?v=QH2-TGUlwu4;}' /etc/nginx/sites-available/default",
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
