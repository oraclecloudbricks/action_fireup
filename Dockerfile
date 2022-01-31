# Copyright (c) 2022 Oracle and/or its affiliates.
FROM python:3.8.2-alpine

COPY action_builder.sh /action_builder.sh
COPY actions/ /actions

ENTRYPOINT ["sh", "/action_builder.sh"]