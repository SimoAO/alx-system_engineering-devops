# Automate puppet to fix apache error
exec { 'fix wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
