# increased number of files that can be opened
exec { 'limit on open files':
    path	=> '/bin',
    command	=> "sed -i 's/15/10000/g' /etc/default/nginx; /etc/init.d/nginx restart"
}
