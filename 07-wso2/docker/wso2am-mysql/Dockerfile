FROM wso2/wso2am:4.7.0

USER root

COPY --chown=wso2carbon:wso2 \
    mysql-connector-j-9.4.0.jar \
    /home/wso2carbon/wso2am-4.7.0/repository/components/lib/

USER wso2carbon
