# Update Nginx file descriptor limit and restart service
exec { 'increase nginx file limit':
  onlyif   => 'test -f /etc/default/nginx',
  command  => "sed -i 's/-n 15/-n 4096/' /etc/default/nginx && service nginx restart",
  provider => 'shell',
}
