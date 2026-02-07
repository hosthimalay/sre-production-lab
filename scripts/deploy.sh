#!/bin/bash
set -e

eksctl create cluster -f infra/eks/cluster.yaml
kubectl apply -f app/k8s/
