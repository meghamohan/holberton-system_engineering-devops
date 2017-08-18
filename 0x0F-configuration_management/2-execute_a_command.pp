# create a manifest that kills a process killmenow
exec { 'killmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin'
}
