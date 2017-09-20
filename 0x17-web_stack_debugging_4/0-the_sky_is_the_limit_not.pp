# increased number of files that can be opened
exec { 'increase limit on open files':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/15/15000/g' /etc/default/nginx; sudo service nginx restart;"
}
