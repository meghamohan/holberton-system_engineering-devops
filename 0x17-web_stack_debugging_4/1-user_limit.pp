# increased number of files that can be opened
exec { 'set user specific FD limit':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/1000/10240/g' /etc/security/limits.conf; sed -i 's/800/4096/g' /etc/security/limits.conf; sudo reboot;"
}
