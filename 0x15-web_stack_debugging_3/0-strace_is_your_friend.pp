# puppet script to fix 500 error
exec { 'Fix /var/www/html/wp-settings':
  path    => ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/locale.phpp/locale.php/' /var/www/html/wp-settings.php"
}
