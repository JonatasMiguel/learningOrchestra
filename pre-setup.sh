#!/bin/bash
echo "--------------------------------------------------------------------"


apt-get update -y

apt-get install nfs-kernel-server -y

mkdir /nfs-learningOrchestra

touch /nfs-learningOrchestra/file1.txt

chown nobody:nogroup /nfs-learningOrchestra

chmod 755 /nfs-learningOrchestra

echo "Configure o nfs-server exports:"
echo "nano /etc/exports"
echo "/nfs-learningOrchestra    nfs-client-ip(rw,sync,no_subtree_check)"
echo "systemctl restart nfs-server"
echo "systemctl status nfs-server"
echo "--------------------------------------------------------------------"
echo "--------------------------------------------------------------------"