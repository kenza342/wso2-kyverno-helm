FROM eclipse-temurin:21-jdk

ENV WSO2_SERVER_HOME=/home/wso2carbon/wso2am-4.7.0

USER root

RUN useradd -ms /bin/bash wso2carbon

COPY --chown=wso2carbon:wso2carbon wso2am-4.7.0 ${WSO2_SERVER_HOME}

RUN chmod +x ${WSO2_SERVER_HOME}/bin/*.sh && \
    chmod +x ${WSO2_SERVER_HOME}/diagnostics-tool/bin/*.sh && \
    chown -R wso2carbon:wso2carbon /home/wso2carbon

USER wso2carbon

WORKDIR ${WSO2_SERVER_HOME}

EXPOSE 9443 9763 8243 8280

ENTRYPOINT []

CMD ["/home/wso2carbon/wso2am-4.7.0/bin/api-manager.sh"]
