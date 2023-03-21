#include "mainwindow.hpp"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow) {

    ui->setupUi(this);
    move(screen()->geometry().center() - frameGeometry().center());

    setWindowTitle("Sem Título - Bloco de anotações");
    this->setCentralWidget(ui->textEdit);
}

MainWindow::~MainWindow() { delete ui; }

void MainWindow::on_actionNovo_triggered() {
    current_file.clear();
    setWindowTitle("Sem Título - Bloco de anotações");
    ui->textEdit->setText(QString());
}

void MainWindow::on_actionAbrir_triggered() {
    QString file_name = QFileDialog::getOpenFileName();
    QFile file(file_name);
    current_file = file_name;

    if (!file.open(QIODevice::ReadOnly | QFile::Text)) {
        QMessageBox::warning(this, "Aviso: ",
                             "Não foi possível abrir o arquivo " +
                                 file.errorString());
        return;
    }

    setWindowTitle(file_name + " - Bloco de anotações");

    QTextStream in(&file);
    QString text = in.readAll();
    ui->textEdit->setText(text);
    file.close();
}

void MainWindow::on_actionSalvar_triggered() {
    QString file_name = QFileDialog::getSaveFileName();
    QFile file(file_name);
    current_file = file_name;

    if (!file.open(QIODevice::WriteOnly | QFile::Text)) {
        QMessageBox::warning(this, "Aviso: ",
                             "Não foi possível salvar o arquivo " +
                                 file.errorString());
        return;
    }

    setWindowTitle(file_name + " - Bloco de anotações");

    QTextStream out(&file);
    QString text = ui->textEdit->toPlainText();
    out << text;
    file.close();
}

void MainWindow::on_actionSair_triggered() { QApplication::quit(); }

void MainWindow::on_actionCopiar_triggered() {}

void MainWindow::on_actionColar_triggered() {}

void MainWindow::on_actionRecortar_triggered() {}

void MainWindow::on_actionDesfazer_triggered() {}

void MainWindow::on_actionRefazer_triggered() {}

void MainWindow::on_actionSobre_o_aplicativo_triggered() {
    QMessageBox message_about;

    message_about.setWindowTitle("Sobre");
    message_about.setText("<h3 align='center'><pre>\tFeito por Lucas "
                          "Turos\t\t\nUtilizando: Qt5 e C++</pre></h3>");
    message_about.exec();
}
