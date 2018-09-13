
# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
node_num = 4
nodes = list()
for i in range(node_num):
	nodes.append(request.XenVM("node"+str(i+1)))
link = request.LAN("lan")
i = 0
for node in nodes:
	 node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
	if i ==0:
		node.routable_control_ip="true"
		node.addService(pg.Execute(shell="/bin/sh", command="sudo local/repository/silly.sh"))
	iface = node.addInterface("if1")
	iface.component_id = "eth1"
	iface.addAddress(pg.IPv4Address("192.168.1."+str(i+1),"255.255.255.0"))
	link.addInterface(iface)
# Install and execute a script that is contained in the repository.
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
