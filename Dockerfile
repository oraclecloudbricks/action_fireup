# Copyright (c) 2022 Oracle and/or its affiliates.
FROM python:3.8.2-alpine

COPY action_builder.sh /action_builder.sh
COPY actions/ /actions

RUN $FILES_ADDED > /files_added
RUN $FILES_MODIFIED > /files_modified
RUN $PR_BODY > /pr_body
RUN $BRANCH_NAME > /branch_name

RUN echo "temp var: "
RUN cat /files_added
RUN cat /files_modified
RUN cat /pr_body
RUN cat /branch_name

ENTRYPOINT ["sh", "/action_builder.sh"]