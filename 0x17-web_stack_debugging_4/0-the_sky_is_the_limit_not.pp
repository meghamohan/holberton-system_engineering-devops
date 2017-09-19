# checked the log, number of files that can be opened
# simulatanously was found to be less.
exec { 'limit on open files':
    path=>'/bin',
    command=>"sed -i 's/15/1001' /etc/default/nginx; /etc/init.d/nginx restart"
  }
