# Install flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install a compatible version of Werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
