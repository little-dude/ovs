import unixctl.client

print "FOO"
err, client = unixctl.client.UnixctlClient.create( "/home/corentih/ovs/custom/var/run/openvswitch/ovs-vswitchd.4959.ctl")
#print conn.__class__.__name__
#client = unixctl.client.UnixctlClient(conn._conn)
foo, err, s = client.transact("vlog/list", [])
#foo, err, s = client.transact("memory/show", [])
#foo, err, s = client.transact("bfd/show", [])
print foo
print err
print s


