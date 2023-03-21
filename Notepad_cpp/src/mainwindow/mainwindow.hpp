#ifndef MAINWINDOW_HPP
#define MAINWINDOW_HPP

#include <QFile>
#include <QScreen>
#include <QMainWindow>
#include <QFileDialog>
#include <QTextStream>
#include <QMessageBox>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
   void on_actionNovo_triggered();
   void on_actionAbrir_triggered();
   void on_actionSalvar_triggered();

   void on_actionSair_triggered();

   void on_actionCopiar_triggered();

   void on_actionColar_triggered();

   void on_actionRecortar_triggered();

   void on_actionDesfazer_triggered();

   void on_actionRefazer_triggered();

   void on_actionSobre_o_aplicativo_triggered();

private:
    Ui::MainWindow *ui;

    QString current_file{};
};
#endif // MAINWINDOW_HPP
