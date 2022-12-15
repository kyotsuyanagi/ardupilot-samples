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
1. SITLで機体を立ち上げます。-> sitl/launch_sitl.pyで４機体立ち上げます。
2. スクリプトがアクセスするためのmavlinkポートやMission Plannerで接続するためのポートを拡張するため、mavproxy.pyで４機のSITLポートを拡張します。 -> sitl/launch_mavproxy.py
3. 機体を動かします。 -> drone/launch_drone.py
4. 機体を監視します。 -> drone/monitor_drone.py
5. 管理スクリプトからパラメータ経由で通知され、パラメータの値で機体を制御します。0は100m以上離れている。1は100m未満に近づいている。 -> lua/receiver.lua


