for fil in $list ; do echo $fil ; fname=`basename $fil` ; dirname=`dirname $fil` ; echo $result $dirname ; newfname=`echo $fname | sed 's/h2ogpuml/h2o4gpu/g'` ; echo $newfname ; git mv $dirname/$fname $dirname/$newfname ; done
