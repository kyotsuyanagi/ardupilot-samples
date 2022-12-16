# ardupilot-samples

## アプリケーションの内容
３機のドロンが上空に待機している中、４機目のドローンが並んでいる３機に衝突しようとした時に４機目のドローンが100m以内に近づいたのを検知したら、監視スクリプトが３機にアクセスしてカスタムパラメータMON_NEARを更新します。<br>
機体の中のluaスクリプトはパラメータMON_NEARの変化を監視しており、１になった場合に機体を１０m移動させて４機目がぶつからないように制御します。<br>
drone/monitor_drone.pyは監視スクリプトになります。<br>
drone/launch_drone.pyは３機が待機し４機が３機のポジションを通過するように動作させるスクリプトです。<br>

## Dronekitのインストール方法
まずはaptのリポジトリのリストを最新のものに更新(update)し，更新のあるものをupgradeします．
```
$sudo apt update
$sudo apt upgrade
```
Python開発ライブラリやインストールに必要なパッケージをインストールします。
```
$sudo apt install python-dev python-pip
```
Dronekitをインストールします。これでDronekitが動作する環境ができました。
```
$pip install dronekit
```

## SITLのインストール
```
$ cd ~
$ git clone https://github.com/ArduPilot/ardupilot
$ cd ardupilot
$ git submodule update --init --recursive
$ ~/ardupilot/Tools/environment_install/install-prereqs-ubuntu.sh -y
```

## アプリケーションの実行手順
1. SITLで４機体立ち上げます。スクリプトがアクセスするためのmavlinkポートやMission Plannerで接続するためのポートを拡張するため、mavproxy.pyで４機のSITLポートを拡張します。 -> sitl/launch_sitl.py
2. 機体を動かします。３機は上空で停止し１機は３機に向かって飛行します。 -> drone/launch_drone.py
3. 機体を監視します。向かってくる機体の距離が100m以内になると、監視している機体のカスタムパラメータ[MON_NEAR]を変更し通知します。-> drone/monitor_drone.py 
4. 管理スクリプトからカスタムパラメータ[MON_NEAR]の値の変更があった場合、機体を制御します。0は100m以上離れている。1は100m未満に近づいている。 -> lua/receiver.lua

## デモ動画
https://vimeo.com/781835282