# yaml_to_env
Python module for converting yaml configuration to environment variables


This is heavily based on https://gist.github.com/bcopy/a12c8b5eb01fc606beac4463128a04fd

# Usage
Please see requirements, setup virutal env or something similar, and make sure you have required packages installed.

Just python3 yaml_to_env.py should do the trick, as you should see how it is used.

For attached example config.yml file below show some usage patterns:

```
python3 yaml_to_env.py -f example_config.yml -e DW_ -t dockerenv
DW_SERVER_ADMINCONNECTORS_COUNT=1
DW_SERVER_ADMINCONNECTORS_0_PORT=43567
DW_SERVER_ADMINCONNECTORS_0_TYPE='http'
DW_SERVER_APPLICATIONCONNECTORS_COUNT=1
DW_SERVER_APPLICATIONCONNECTORS_0_PORT=43568
DW_SERVER_APPLICATIONCONNECTORS_0_TYPE='http'
DW_SERVER_SHUTDOWNGRACEPERIOD='120s'
DW_SWAGGER_ENABLED='True'
DW_SWAGGER_RESOURCEPACKAGE='com.some.resource.package'
DW_SWAGGER_SCHEMES_COUNT=2
DW_SWAGGER_SCHEMES_0='https'
DW_SWAGGER_SCHEMES_1='http'
DW_SWAGGER_TITLE='service-fancy-app'
```

```
python3 yaml_to_env.py -f example_config.yml -e DW_ -t export
export DW_SERVER_ADMINCONNECTORS_COUNT=1
export DW_SERVER_ADMINCONNECTORS_0_PORT=43567
export DW_SERVER_ADMINCONNECTORS_0_TYPE='http'
export DW_SERVER_APPLICATIONCONNECTORS_COUNT=1
export DW_SERVER_APPLICATIONCONNECTORS_0_PORT=43568
export DW_SERVER_APPLICATIONCONNECTORS_0_TYPE='http'
export DW_SERVER_SHUTDOWNGRACEPERIOD='120s'
export DW_SWAGGER_ENABLED='True'
export DW_SWAGGER_RESOURCEPACKAGE='com.some.resource.package'
export DW_SWAGGER_SCHEMES_COUNT=2
export DW_SWAGGER_SCHEMES_0='https'
export DW_SWAGGER_SCHEMES_1='http'
export DW_SWAGGER_TITLE='service-fancy-app'
```

```
python3 yaml_to_env.py -f example_config.yml -t export
export SERVER_ADMINCONNECTORS_COUNT=1
export SERVER_ADMINCONNECTORS_0_PORT=43567
export SERVER_ADMINCONNECTORS_0_TYPE='http'
export SERVER_APPLICATIONCONNECTORS_COUNT=1
export SERVER_APPLICATIONCONNECTORS_0_PORT=43568
export SERVER_APPLICATIONCONNECTORS_0_TYPE='http'
export SERVER_SHUTDOWNGRACEPERIOD='120s'
export SWAGGER_ENABLED='True'
export SWAGGER_RESOURCEPACKAGE='com.some.resource.package'
export SWAGGER_SCHEMES_COUNT=2
export SWAGGER_SCHEMES_0='https'
export SWAGGER_SCHEMES_1='http'
export SWAGGER_TITLE='service-fancy-app'
```

```
cat example_config.yml | python3 yaml_to_env.py -e DW_ -t export
export DW_SERVER_ADMINCONNECTORS_COUNT=1
export DW_SERVER_ADMINCONNECTORS_0_PORT=43567
export DW_SERVER_ADMINCONNECTORS_0_TYPE='http'
export DW_SERVER_APPLICATIONCONNECTORS_COUNT=1
export DW_SERVER_APPLICATIONCONNECTORS_0_PORT=43568
export DW_SERVER_APPLICATIONCONNECTORS_0_TYPE='http'
export DW_SERVER_SHUTDOWNGRACEPERIOD='120s'
export DW_SWAGGER_ENABLED='True'
export DW_SWAGGER_RESOURCEPACKAGE='com.some.resource.package'
export DW_SWAGGER_SCHEMES_COUNT=2
export DW_SWAGGER_SCHEMES_0='https'
export DW_SWAGGER_SCHEMES_1='http'
export DW_SWAGGER_TITLE='service-fancy-app'
```

```python3 yaml_to_env.py -e DW_ -t export
No input file provided (-f option), and nothing is piped to a script!
```
