FROM fluentd:latest

USER root

RUN ["gem", "install", "fluent-plugin-elasticsearch"]
RUN ["gem", "install", "fluent-plugin-record-modifier"]

USER fluent