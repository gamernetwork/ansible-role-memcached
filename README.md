# Memcached role for ansible

Role to install memcached packages and configure memcached instances.

## Requirements

Ansible 2.2 or higher is required as this role uses the `systemd` module.

Only Debian based systems that use systemd are supported.

## Instance configuration

Each new `memcached` instance is configured using a new systemd service unit.
No config file is used.

A default service unit template is provided and covers may of the options given
in the man page. An optional service template can be used by setting
`memcached_service_src`.


### Overridable variables

These are the most likely variables that will get overriden when calling the
memcached role.

variable           | default
-------------------|--------
memcached_instance | memcached
memcached_user     | memcache

Look in defaults for other overridable vars.


### Optional run time CLI flags

Set these role variables to `True` to be include in the service unit.

memcached flag | varible
---------------|-----------------
      -k       | memcached_lock_down_paged_memory
      -M       | memcached_oom_error
      -r       | memcached_max_core_file
      -C       | memcached_disable_cas
      -L       | memcached_large_pages


### Optional run time CLI arguments

Define these role variables to be used in the service unit.

memcached option | variable
-----------------|------------------
       -s        | memcached_unix_socket
       -a        | memcached_unix_socket_perms
       -l        | memcached_listen_address
       -m        | memcached_memory
       -c        | memcached_maxconn
       -R        | memcached_seq_reqs
       -k        | memcached_lock_down_paged_memory
       -p        | memcached_listen_port_tcp
       -U        | memcached_listen_port_udp
       -f        | memcached_chunk_factor
       -n        | memcached_min_key_size
       -C        | memcached_unix_socket_perms
       -v        | memcached_verbosity (can be -vv or -vvv)
       -t        | memcached_threads
       -D        | memcached_delimiter
       -B        | memcached_proto
       -o        | memcached_experimental_options


## Tags

Tags can be given to only install or configure a memcache instance..

 * memcached_install
 * memcached_instance


## Example

See `playbook.yml`.


## Testing

Testing is done using [molecule](http://molecule.readthedocs.io/) along with
a [vagrant](https://www.vagrantup.com/) driver and the
[testinfra](https://testinfra.readthedocs.io/) verifier.

Given a working `molecule` and `testinfra` install, running `molecule test` in
the role root driectory will verify the role. Other platforms are availble in
`molecule.yml`.

Currently testing is fairly basic.


## License

GPLv3
