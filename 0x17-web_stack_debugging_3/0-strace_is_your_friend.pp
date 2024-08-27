# Puppet manifest to resolve a WordPress issue causing Apache 500 error
exec { 'repair-wordpress':
  command => 'bash -c "sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php && service apache2 restart"',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
