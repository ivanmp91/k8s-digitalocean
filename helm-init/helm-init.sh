#!/bin/bash
kubectly apply -f tiller-rbac-config.yaml
helm init --upgrade --service-account tiller
