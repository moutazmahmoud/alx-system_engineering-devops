# Adjust user file descriptor limits in configuration
exec { 'increase user file limit to 100 (nofile 5)':
  command => "sed -i 's/nofile 5/nofile 100/' /etc/security/limits.conf",
  path    => '/bin',
}

# Adjust user file descriptor limits in configuration
exec { 'increase user file limit to 100 (nofile 4)':
  command => "sed -i 's/nofile 4/nofile 100/' /etc/security/limits.conf",
  path    => '/bin',
}
